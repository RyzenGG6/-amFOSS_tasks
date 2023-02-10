import 'package:flame/components.dart';
import 'package:flutter/services.dart';
import 'package:flame/game.dart';
import 'package:flame/palette.dart';
import 'package:flutter/cupertino.dart';

void main() {
  print('loading the game widgets');
  runApp(GameWidget(game: MyGame()));
  SystemChrome.setPreferredOrientations([DeviceOrientation.landscapeLeft]);
  SystemChrome.setPreferredOrientations([DeviceOrientation.landscapeRight]);
}
class MyGame extends FlameGame with HasDraggables {
  SpriteComponent bunny = SpriteComponent();
  SpriteComponent background = SpriteComponent();
  final Vector2 buttonSize = Vector2(50, 50);
  final double charactersize = 175;
  @override
  late final JoystickComponent joystick;


  Future<void> onLoad() async {
    super.onLoad();
    final screenWidth = size;
    final screenHeight = size;
    add(background);
      ..sprite = await loadSprite('background.png')
      ..size = size);
    bunny
      ..sprite = await loadSprite('bunny.png')
      ..size = Vector2(charactersize, charactersize)
      ..x = 300
      ..y = 200;
    add(bunny);
    final knobPaint = BasicPalette.blue.withAlpha(200).paint();
    final backgroundPaint = BasicPalette.white.withAlpha(100).paint();
    joystick = JoystickComponent(
      knob: CircleComponent(radius: 18, paint: knobPaint),
      background: CircleComponent(radius: 50, paint: backgroundPaint),
      margin: const EdgeInsets.only(left: 40, bottom: 40),);
    add(joystick);
  }

  @override
  update(double dt) {
    super.update(dt);
    bunny.position.add(joystick.relativeDelta * 200 * dt);
  }
}